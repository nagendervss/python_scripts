import argparse, os, cv2

def parser():

    args_parser = argparse.ArgumentParser(description='Given a list of video files, count the number of files for each fps.')

    args_parser.add_argument('--root_dir', type=str, default='/mnt/data2/datasets/Youtube_Dataset/videos_ted_clips/', help='Path to the root directory. The list of files are assumed to have relative paths from this root directory')
    args_parser.add_argument('--file_list_path', type=str, default='/mnt/data2/datasets/Youtube_Dataset/videos_ted_clips/clip_list.txt', help='Path to the file containing the list of video files.')
    args_parser.add_argument('--print_cont_count', action='store_true', help='Print the count of files with fps continuously.')
    
    args = args_parser.parse_args()

    return args

if __name__=='__main__':

    args = parser()

    # Read the file paths
    list_file_handler = open(args.file_list_path, 'r')
    relative_path_list = list_file_handler.readlines()
    relative_path_list = [s.strip() for s in relative_path_list]
    list_file_handler.close()

    absolute_path_list = [os.path.join(args.root_dir, s) for s in relative_path_list]

    # Reading fps
    fps_dict = {}
    for video_path in absolute_path_list:

        video_cap = cv2.VideoCapture(video_path)
        fps = video_cap.get(cv2.CAP_PROP_FPS)
        video_cap.release()
        if fps==0:
            print(f'Video with 0 fps: {video_path}')
        if fps in fps_dict.keys():
            fps_dict[fps] += 1
        else:
            fps_dict[fps] = 1
        
        if args.print_cont_count:
            print_str = ''
            for key,value in fps_dict.items():
                print_str += f'{key}:{value}; '
            print(print_str, end='\r')
    
    # Final output
    for key,value in fps_dict.items():
        print_str += f'{key}:{value}; '
    print(print_str)

