import glob, subprocess, argparse, tqdm

def parser():

    args_parser = argparse.ArgumentParser(description='script to delete all files that match the input pattern')

    args_parser.add_argument('--pattern', type=str, required=True, help='The regex of the files to be deleted.')

    args = args_parser.parse_args()

    return args

if __name__=='__main__':

    args = parser()

    print('Reading paths of files to be deleted.')
    file_lst = glob.glob(args.pattern)

    print('Deleting files.')
    for file in tqdm.tqdm(file_lst):
        cmd = f'rm {file}'
        subprocess.run(cmd, shell=True)