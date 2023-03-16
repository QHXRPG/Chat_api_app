import subprocess
import json
import os
import uuid

class chat_model:
    def __init__(self):
        self.a = None
        self.curl_command=None
        self.result=None
        self.file_name =None
        self.time_uuid = uuid.uuid1()
    def built_json(self):
        self.file_name = 'chat_App_win.json'
        data = {"model": "gpt-3.5-turbo",
                "temperature": 0.7,
                "max_tokens": 200,
                "apiKey": "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",
                "content": self.a,
                "sessionId": str(self.time_uuid)}
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    def delete_json(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
    def chat(self,a):
        self.a = a
        self.a = self.a.replace('\n', ' ')
        self.built_json()
        self.curl_command = """curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer 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" --data "@chat_App_win.json" https://api.openai-proxy.com/v1/chat/completions"""
        process = subprocess.Popen(self.curl_command, stdout=subprocess.PIPE, shell=True)
        self.result, error = process.communicate()
        self.result1 = self.result.decode('utf-8')
        self.result = self.result1.split("""":""")[-1]
        self.result = self.result.replace("}",'').replace('\\n','\n').replace('"','')
        self.delete_json()
