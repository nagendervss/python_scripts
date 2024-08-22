import argparse, os, cv2, tqdm
from tools import stats_list

def parser():

    args_parser = argparse.ArgumentParser(description='Find the mean and std dev of the properties of video files')

    args_parser.add_argument('--root_dir', type=str, default='/mnt/data2/datasets/Youtube_Dataset/videos_ted_clips/', help='Path to the root directory. The list of files are assumed to have relative paths from this root directory')
    args_parser.add_argument('--file_list_path', type=str, default='/mnt/data2/datasets/Youtube_Dataset/videos_ted_clips/clip_list.txt', help='Path to the file containing the list of video files.')

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

    fps_stats = stats_list()
    dur_stats = stats_list()
    width_stats = stats_list()
    height_stats = stats_list()

    for video_path in tqdm.tqdm(absolute_path_list):

        video_cap = cv2.VideoCapture(video_path)

        if video_cap.isOpened():

            fps = video_cap.get(cv2.CAP_PROP_FPS)
            num_frames = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)
            dur = num_frames/fps
            width = video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

            fps_stats.append(fps)
            dur_stats.append(dur)
            width_stats.append(width)
            height_stats.append(height)
        
        video_cap.release()

    fps_min = fps_stats.get_min()
    fps_max = fps_stats.get_max()
    fps_mean = fps_stats.get_mean()
    fps_stddev = fps_stats.get_stdev()
    print(f'fps: min: {fps_min}; max: {fps_max}; mean: {fps_mean}; stdev: {fps_stddev}')
    
    dur_min = dur_stats.get_min()
    dur_max = dur_stats.get_max()
    dur_mean = dur_stats.get_mean()
    dur_stddev = dur_stats.get_stdev()
    print(f'dur: min: {dur_min}; max: {dur_max}; mean: {dur_mean}; stdev: {dur_stddev}')

    width_min = width_stats.get_min()
    width_max = width_stats.get_max()
    width_mean = width_stats.get_mean()
    width_stddev = width_stats.get_stdev()
    print(f'width: min: {width_min}; max: {width_max}; mean: {width_mean}; stdev: {width_stddev}')

    height_min = height_stats.get_min()
    height_max = height_stats.get_max()
    height_mean = height_stats.get_mean()
    height_stddev = height_stats.get_stdev()
    print(f'height: min: {height_min}; max: {height_max}; mean: {height_mean}; stdev: {height_stddev}')

    total_num = len(fps_stats.lst)
    print(f'Total Number: {total_num}')