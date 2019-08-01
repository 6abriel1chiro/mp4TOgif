import imageio
import os
clip = os.path.abspath('codeblog.mp4') #name of the video file to convert 

def ToGif(inputPath,targetFormat): #targetFormat must be .gif
    outputPath=os.path.splitext(inputPath)[0] + targetFormat # 'codeblog'  'mp4'

    print('converting ',inputPath,' to ',outputPath)

    reader=imageio.get_reader(inputPath)
    fps=reader.get_meta_data()['fps']
    writer=imageio.get_writer(outputPath, fps=fps)
    for frames in reader:
        writer.append_data(frames)
        #print(f'frame: {frames}')

    print("Done")
    writer.close()
ToGif(clip,'.gif')