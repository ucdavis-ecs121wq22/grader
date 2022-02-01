input=$1
d="_$((1 + $RANDOM % 100))"
mkdir -p $d
echo "import importlib" > $d/test_all.py
echo "_ = importlib.import_module('_')" >> $d/test_all.py
cat test/test_all.py >> $d/test_all.py
touch $d/__init__.py
sed -i "s/src/_/g" $d/test_all.py
if [ $(pytest $d -k $input | grep $input | grep "^FAILED" | wc -l) -eq "1" ];
then
    echo "pass";
    rm -rf $d;
    exit 0;
else echo "fail";
    rm -rf $d;
    exit 0;
fi