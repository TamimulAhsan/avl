from pytube import YouTube
from pytube.cli import on_progress
def youtube(link):
    print("                 _______                 ")
    print("                / _____ \\               | |  ")
    print("               / /     \\ \\              | |    ")
    print("              / /       \\ \\             | |     ")
    print("             / /         \\ \\            | |   ")
    print("            / /           \\ \\           | |   ")
    print("           / /_____________\\ \\          | |   ")
    print("          / _________________ \\         | |   ")
    print("         / /                 \\ \\        | |   ")
    print("        / /    \\        /     \\ \\       | |   ")
    print("       / /      \\      /       \\ \\      | |   ")
    print("      / /        \\    /         \\ \\     | |   ")
    print("     / /          \\  /           \\ \\    | |_______________  ")
    print("    / /            \\/             \\ \\   |_________________|  ")

    print("\n\n\n\n\t\t\tAdvanced Video Loader.\n\n")
    print('Seaching..... Please wait')

    try:
        yt = YouTube(link,on_progress_callback=on_progress)
    except Exception as e:
        print('Video not found.')
    else:
        video_streams = list()

        for stream in yt.streams:
            if stream.resolution is not None:
                video_streams.append(stream)

        resolutions_with_fps = list(set([f"{stream.resolution} {stream.fps}" for stream in video_streams]))

        for i , j in enumerate(resolutions_with_fps, start=1):
            print(f'{i}. {j}fps')

        invalid = True
        while invalid:
            video_selection = input('Resolution (leave blank for 720p): ')
            if video_selection != "":
                try:
                    int_video_selection = int(video_selection)
                    res_and_fps = resolutions_with_fps[int_video_selection-1].split()
                    res = res_and_fps[0]
                    # fps = int(res_and_fps[1])
                    video = yt.streams.get_by_resolution(res)
                except Exception as e:
                    print('Invalid Choice. Please choose agian: ')
                    invalid = True
                else:
                    invalid = False   
            else:
                video = yt.streams.get_by_resolution("720p")
            break

        filename = input('Filename (leave blank for default): ')

        print('Download Started... Please wait..\n')
        try:
            if filename != "":
                video.download(filename=filename)
                print("")
            else:
                video.download()
        except Exception as e:
            print("An error occured. Please Try again.")
        else:
            print('\nDownload Finished')

link = input('\nEnter video link: ')
youtube(link)
