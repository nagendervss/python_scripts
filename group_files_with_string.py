import os, argparse, sys, subprocess, tqdm

def parser():

    args_parser = argparse.ArgumentParser(description='Script to collect all files with a common string at the specified position in the string.')

    args_parser.add_argument('--source_dir', type=str, required=True, help='Path to the directory containing the files to be grouped.')
    args_parser.add_argument('--target_dir', type=str, help='Path to the directory to save the grouped files. Defaults to the source directory.')
    args_parser.add_argument('--copy', action='store_true', help='Copies the files from the source directory to the target directory.')
    args_parser.add_argument('--move', action='store_true', help='Moves the files from source directory to the target directory. Defaults to copy in case of ambiguity in options.')
    args_parser.add_argument('--delimiter', type=str, required=True, help='Delimiter to split the file names in the source directory. One of the resulting list of strings should be the grouping string.')
    args_parser.add_argument('--index', type=int, required=True, help='Index of the grouping string in the name parts of the filename.')

    args = args_parser.parse_args()

    return args

if __name__=='__main__':

    args = parser()

    if args.target_dir is None:
        args.target_dir = args.source_dir
    
    if ((args.copy is None) and (args.move is None)) or (args.copy and args.move):
        args.copy = True
        args.move = False

    source_file_list = os.listdir(args.source_dir)
    grouping_strings = []

    for file_name in tqdm.tqdm(source_file_list):
        file_name_parts = file_name.split(args.delimiter)
        if len(file_name_parts) == 1:
            continue
        local_grouping_string = file_name_parts[args.index]
        group_dir_path = os.path.join(args.target_dir, local_grouping_string)
        os.makedirs(group_dir_path, exist_ok=True)

        if args.copy:
            file_transfer_cmd = 'cp'
        elif args.move:
            file_transfer_cmd = 'mv'
        else:
            print('Please select either copy or move to transfer the files.')
            sys.quit()
        
        source_file_path = os.path.join(args.source_dir, file_name)
        target_file_path = os.path.join(args.target_dir, group_dir_path, file_name)
        cmd = f'{file_transfer_cmd} "{source_file_path}" "{target_file_path}"'
        print(cmd)
        subprocess.run(cmd, shell=True)