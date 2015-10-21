#!/Users/yukitomo/.pyenv/versions/chainer_py343/bin/python
#-*-coding:utf-8-*-
#2015-10-20 Yuki Tomo

"""
How to Use
$ python3 eval.py ws_ref ws_out
"""

import sys
from argparse import ArgumentParser

def label_chars(sent):
	chars_labels = []
	for char in sent:
		if char == " ":
			label = "B"
		else:
			chars.append((char,label))
			label = "I"
	return chars_labels




def calc_scores(ref_file, rslt_file):
	N_ref = 0 #reference 中のフレーズ数
	N_rslt = 0 #result 中のフレーズ数
	N_cor = 0 #result 中の正解フレーズ数
 
	with open(ref_file) as ref, open(rslt_file) as rslt:
		for i, sent_ref, sent_rslt in  zip(enumerate(ref), rslt):
			#split_phrases
			chars_ref = label_chars(sent_ref.strip())
			chars_rslt = label_chars(sent_rslt.strip())

			if len(chars_ref) != len(chars_rslt):
				print(i)
				print("ref_sent :", sent_ref)
				print("rslt_sent :", sent_rslt)  
				raise ValueError("ref and rslt doesn't match about characters")

			n_cor = 0 #result出力の今見ているsentence中の正解フレーズ数
		
			for char_ref, char_rslt in ziP(chars_ref, char_rslt):
				


	return precision, recall F

def parse_args():

    p = ArgumentParser(description='Word segmentation using LSTM-RNN')

    p.add_argument('ref', help='reference file')
    p.add_argument('rslt', help='system result')

    args = p.parse_args()

    # check args
    try:
        if args.ref == "": raise ValueError('you must set ref = reference')
        if args.rslt == "": raise ValueError('you must set rslt = system result')

    except Exception as ex:
        p.print_usage(file=sys.stderr)
        print(ex, file=sys.stderr)
        sys.exit()

    return args

def main():
	args = parse_args()

	print("reference :", args.ref)
	print("result    :", args.rslt)

	precision, recall, F = calc_scores(args.ref, args.rslt) 

if __name__ == '__main__':
	main()

