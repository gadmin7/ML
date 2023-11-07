import argparse
import pandas as pd
import math

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument("train_input", type=str, help='path to training input .tsv file')
    parser.add_argument("inspection_output", type=str)
    parser.add_argument("target", type=str)

    args = parser.parse_args()
    df = pd.read_csv(args.train_input,sep='\t')
    classes = list(df[args.target].unique())

    entropy = 0 

    for cls in classes:
        fraction_cls = df[args.target].eq(cls).mean()
        entropy = entropy + (fraction_cls*math.log(fraction_cls,2))
    entropy = entropy * -1
    text1 = "entropy : "+str(entropy)+"\n"

    error = (df.shape[0] - df[args.target].value_counts()[0])/df.shape[0]
    text2 = "error : "+str(error)

    with open(args.inspection_output, 'w') as f:
        f.write(text1)
        f.write(text2)

    print("entropy : ",entropy)
    print("error : ",error)