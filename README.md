# pythonrouge
This is the python script to use [ROUGE](http://www.berouge.com/Pages/default.aspx), summarization evaluation toolkit.
  
In this implementation, you can evaluate ROUGE-1, ROUGE-2, ROUGE-3, ROUGE-SU4, and ROUGE-L. You can evaluate your model summary with a peer summary right now. It's not necessary to make an xml file as in the general ROUGE package.

Any feedbacks or comments are welcome.

**To compare an automatically generated summary with a reference file, please take a look at [file2rouge](https://github.com/pltrdy/files2rouge)**

# Getting Started

**1) Clone & Install**
```
# clone
git clone https://github.com/pltrdy/pythonrouge.git

# install using pip
sudo python setup.py install
```

**2) Import and use**
The only things you need to evaluate ROUGE score is to specify the paths of ROUGE-1.5.5.pl and RELEASE-1.5.5/data in this package.

```python
from pythonrouge import pythonrouge

ROUGE = sys.argv[1] #ROUGE-1.5.5.pl
data_path = sys.argv[2] #data folder in RELEASE-1.5.5
peer = " Tokyo is the one of the biggest city in the world."
model = "The capital of Japan, Tokyo, is the center of Japanese economy."
score = pythonrouge(ROUGE, data_path, model, peer)
print(score)
```

Output:
```json
{"F": {
  "ROUGE-1": 0.64516,
  "ROUGE-2": 0.55172,
  "ROUGE-3": 0.44444,
  "ROUGE-L": 0.38709,
  "ROUGE-S4": 0.384},
"P": {
  "ROUGE-1": 1.0,
  "ROUGE-2": 0.88889,
  "ROUGE-3": 0.75,
  "ROUGE-L": 0.6,
  "ROUGE-S4": 0.68571},
"R": {
  "ROUGE-1": 0.47619,
  "ROUGE-2": 0.4,
  "ROUGE-3": 0.31579,
  "ROUGE-L": 0.28571,
  "ROUGE-S4": 0.26667}
}
```

See and run `example.py`

# Known Issues

## 1.1 `Cannot open exception db file for reading`
i.e.
```
Cannot open exception db file for reading: /home/pythonrouge/pythonrouge/RELEASE-1.5.5/data/WordNet-2.0.exc.db
```

## 1.2 `CalledProcessError : returned non-zero exit status 255`
i.e. 
```
$ python example.py 
```
Outputs:   
```
Peer summary:   Tokyo is the one of the biggest city in the world.
Model summary:  The capital of Japan, Tokyo, is the center of Japanese economy.
Traceback (most recent call last):
  File "example.py", line 11, in <module>
    score = pythonrouge(peer, model)
  File "/<HOME>/pythonrouge/pythonrouge.py", line 65, in pythonrouge
    output = subprocess.check_output([ROUGE_path, "-e", data_path, "-a", "-m", "-2", "4","-n", "3", abs_xml_path], stderr=subprocess.STDOUT)
  File "/usr/lib/python2.7/subprocess.py", line 573, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
subprocess.CalledProcessError: Command '['/<HOME>/pythonrouge/RELEASE-1.5.5/ROUGE-1.5.5.pl', '-e', '/<HOME>/pythonrouge/RELEASE-1.5.5/data', '-a', '-m', '-2', '4', '-n', '3', '/tmp/tmp63TboY/rouge.xml']' returned non-zero exit status 255
```

## Fixing 1.1 and 1.2
You may solve the two issues above by running:
```
cd pythonrouge/RELEASE-1.5.5/data/
rm WordNet-2.0.exc.db
./WordNet-2.0-Exceptions/buildExeptionDB.pl ./WordNet-2.0-Exceptions ./smart_common_words.txt ./WordNet-2.0.exc.db
```
