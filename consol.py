import subprocess

hosts = ["google.com"]

for host in hosts:
    res = subprocess.run(["ping",host],stdout=subprocess.PIPE)

    print(res.stdout.decode("cp932"))
    
    if res.returncode == 0 :
        print("成功\n\n")
    else:
        print("失敗\n\n")
    print("-----------------------------")