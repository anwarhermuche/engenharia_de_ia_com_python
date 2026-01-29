import pandas as pd
import json

class ETL:

    def __init__(self, path: str = "./modulo_6/support_logs_dirty.csv"):
        self.path = path
        self.df = pd.read_csv(path)

    def normalize_content(self, df: pd.DataFrame) -> pd.DataFrame:
        sender_map = {
            "cliente": "human",
            "assistant": "ai",
            "bot": "ai",
            "ai": "ai",
            "human": "human"
        }

        df_v1 = df.dropna(subset = ["sender"])
        df_v1 = df_v1[df_v1['sender'] != 'system']
        df_v1['sender'] = df_v1['sender'].str.lower()
        df_v1['sender'] = df_v1['sender'].map(sender_map)
        df_v2 = df_v1.dropna(subset = ["content"])
        df_v2 = df_v2[df_v2['content'].str.len() > 15]
        return df_v2

    def regex_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        # Regexs
        regex_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        regex_phone = r'\b(?:\(?\d{2}\)?\s?)?(?:9\d{4}|\d{4})[-\s]?\d{4}\b'
        regex_cpf = r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b'
        pii_pattern = f'({regex_email}|{regex_phone}|{regex_cpf})'

        # Mascarar PII na coluna 'content' com 'x's de mesmo comprimento
        df_v3 = df.copy()

        df_v3['content'] = df_v3['content'].str.replace(pii_pattern, lambda match: 'x' * len(match.group(0)), regex=True)

        df_v3['content'] = df_v3['content'].str.strip().replace(r'<[^>]*>', '', regex=True).replace(r'\s+', ' ', regex=True)

        return df_v3

    def cleaning_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df_v4 = df[df['created_at'] != 'invalid_date'].copy()
        df_v4['created_at'] = pd.to_datetime(df_v4['created_at'], format='mixed', errors='coerce', utc=True).dt.tz_localize(None)
        df_v4['created_at'] = df_v4['created_at'].dt.strftime("%d/%m/%Y %H:%M:%S")
    
        df_v5 = df_v4.drop_duplicates(subset = ["content"])
        df_v6 = df_v5.sort_values(['chat_id', 'created_at'])

        return df_v6

    def df_to_list(self, df: pd.DataFrame) -> list:
        jsons_list = []
        for id, df in df.groupby("chat_id"):
            valores = df[df['chat_id'] == id][["sender", "content"]].values.tolist()
            map_role = {
                "human": "user",
                "ai": "assistant"
            }
            jsons_list.append({"messages": [{"role": map_role[valores[k][0]], "contennt": valores[k][1]} for k in range(len(valores))]})
        
        mensagens_validas = []
        for chat in jsons_list:
            qtd_msgs = len(chat['messages'])
            lista_msgs = list(map(lambda x: x['role'], chat['messages']))

            if ['user', 'assistant']*int(qtd_msgs//2) == lista_msgs:
                mensagens_validas.append(chat)

        return mensagens_validas

    def list_to_jsonl(self, list_obj: list, path: str = "./modulo_6/support_logs.jsonl") -> None:
        with open(path, 'w', encoding='utf-8') as f:
            for chat in list_obj:
                # Garante que a chave seja 'content' (correção de possível typo 'contennt')
                for msg in chat['messages']:
                    if 'contennt' in msg:
                        msg['content'] = msg.pop('contennt')
                
                # Escreve a linha no arquivo JSONL
                json.dump(chat, f, ensure_ascii=False)
                f.write('\n')
        

    def create_json(self):
        df = self.normalize_content(self.df)
        df = self.regex_filters(df)
        df = self.cleaning_data(df)
        lista_objs = self.df_to_list(df)
        self.list_to_jsonl(lista_objs)



       