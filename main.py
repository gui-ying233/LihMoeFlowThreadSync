from os import system, listdir, rename
from json import load, dumps
from time import sleep

while 1:
    newJSON = {}

    for _ in listdir("/Users/guiying/Downloads"):
        if _[:4] == "萌娘百科" and _[-15:] == "flowthread.json":
            try:
                print(_)
                rename("/Users/guiying/Downloads/" + _,
                       "./Lih萌百镜像站flowthread-原.json")
                with open("Lih萌百镜像站flowthread-原.json", "r") as i, open("Lih萌百镜像站flowthread.json", "w") as o:
                    for _ in load(i):
                        newJSON[_["title"]] = _["posts"]
                    i.close()
                    o.write(dumps(newJSON, indent=4))
                    o.close()
            finally:
                try:
                    system('git add ./Lih萌百镜像站flowthread.json')
                    system('git commit -m "Update"')
                    system('git push origin main')
                except Exception as e:
                    print(e)
                finally:
                    print("——" * 10)
                    sleep(3600)
