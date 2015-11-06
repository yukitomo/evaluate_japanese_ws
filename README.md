#evaluate_japanese_ws
スペースで単語分かち書きされたテキストのPrecision, Recall, F値を`conlleval.pl`を利用して算出します。
利用開始前に`conlleval.pl`を以下のようにダウンロードしてください。

```
wget http://www.cnts.ua.ac.be/conll2000/chunking/conlleval.txt -O  conlleval.pl
```

以下のように、正解データ `ref_file`、システム出力ファイル`sys_file`を与えることで評価を行います。
```bash
$ bash  eval_japanese_ws.sh ref_file sys_file
```
