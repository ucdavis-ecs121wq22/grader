#!/bin/bash

cat << EOF > __.py
#!/usr/bin/python3 -tt
from subprocess import check_output
out = str(check_output(["pytest","--cov","--cov-report","term-missing","test/"]), encoding='utf-8')
for line in out.splitlines():
    if "TOTAL" in line:
        cov = int(line.replace('%', '').split()[-1])
        if cov >= int(VALUE):
            print("pass")
        else:
            print("fail")

EOF
sed -i "s/VALUE/$1/g" __.py
chmod 770 __.py
./__.py
rm __.py