# pythonrouge
This is the python script to use ROUGE, summarization evaluation toolkit.
  
In this implementation, you can evaluate ROUGE-1, ROUGE-2, ROUGE-3, ROUGE-SU4, and ROUGE-L. You can evaluate your model summary with a peer summary right now. It's not necessary to make an xml file as in the general ROUGE package.

Any feedbacks or comments are welcome.

# Install
You can install pythonrouge in both ways

```
# not using pip
python setup.py install

# using pip
pip install git+https://github.com/tagucci/pythonrouge.git
```
Then, you can use pythonrouge. If you don't have ROUGE package, I recommend you clone this repository to your local, and do "python setup.py install".

# Usage

The only things you need to evaluate ROUGE score is to specify the paths of ROUGE-1.5.5.pl and RELEASE-1.5.5/data in this package.

```
from pythonrouge import pythonrouge

ROUGE = sys.argv[1] #ROUGE-1.5.5.pl
data_path = sys.argv[2] #data folder in RELEASE-1.5.5
peer = " Tokyo is the one of the biggest city in the world."
model = "The capital of Japan, Tokyo, is the center of Japanese economy."
score = pythonrouge.pythonrouge(ROUGE, data_path, model, peer)
print(score)
```

The output will be below. For convenience, only f_score will be output.

```
{'ROUGE-1': 0.45455, 'ROUGE-2': 0.2, 'ROUGE-3': 0.11111, 'ROUGE-SU4': 0.175, 'ROUGE-L': 0.36364}
```

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
    score = pythonrouge.pythonrouge(peer, model)
  File "/<HOME>/pytohnrouge/pythonrouge/pythonrouge.py", line 65, in pythonrouge
    output = subprocess.check_output([ROUGE_path, "-e", data_path, "-a", "-m", "-2", "4","-n", "3", abs_xml_path], stderr=subprocess.STDOUT)
  File "/usr/lib/python2.7/subprocess.py", line 573, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
subprocess.CalledProcessError: Command '['/<HOME>/pythonrouge/pythonrouge/RELEASE-1.5.5/ROUGE-1.5.5.pl', '-e', '/<HOME>/pythonrouge/pythonrouge/RELEASE-1.5.5/data', '-a', '-m', '-2', '4', '-n', '3', '/tmp/tmp63TboY/rouge.xml']' returned non-zero exit status 255
```

## Fixing 1.1 and 1.2
You may solve the two issues above by running:
```
cd pythonrouge/RELEASE-1.5.5/data/
rm WordNet-2.0.exc.db
./WordNet-2.0-Exceptions/buildExeptionDB.pl ./WordNet-2.0-Exceptions ./smart_common_words.txt ./WordNet-2.0.exc.db
```
