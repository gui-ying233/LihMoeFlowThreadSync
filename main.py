import os
import json

newJSON = {}

for _ in os.listdir("/Users/guiying/Downloads"):
    if _[:4] == "萌娘百科" and _ [-15:] == "flowthread.json":
        try:
            print(_)
            os.rename("/Users/guiying/Downloads/" + _,
                      "./Lih萌百镜像站flowthread-原.json")
            for _ in json.load(open("Lih萌百镜像站flowthread-原.json")):
                newJSON[_["title"]] = _["posts"]
            open("Lih萌百镜像站flowthread.json", "w").write(
                json.dumps(newJSON, indent=4))
        finally:
            try:
                os.system('git add .')
                os.system('git commit -m "Update"')
                os.system('git push origin main')
            except Exception as e:
                print(e)
            finally:
                print("Fin")