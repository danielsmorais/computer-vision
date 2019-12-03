opengl('save','hardware')

v = VideoReade('video_1.mp4');

while hasFrame(v)
    frame = read(v);    
    imshow(frame);    
    pause(1/v.FrameRate)
end