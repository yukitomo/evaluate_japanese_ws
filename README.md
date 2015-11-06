# evaluate_japanese_ws
スペースで単語分かち書きされたテキストのPrecision, Recall, F値をconlleval.plを利用して算出します。
利用開始前にconlleval.plを以下のようにダウンロードしてください。
wget http://www.cnts.ua.ac.be/conll2000/chunking/conlleval.txt -O  conlleval.pl

以下のように、正解データ、システム出力ファイルを与えることで評価を行います。
$ bash  eval_japanese_ws.sh ref_file sys_file

