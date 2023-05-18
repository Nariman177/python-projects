def main():
    num_videos = int(input('Cкoлькo видеоклипов в проекте? '))
    video_file = open('video_times.txt', 'w')
    print('Введите длительность каждого видеоклипа.')
    for count in range(1, num_videos + 1):
        run_time = float(input('Bидeoклип № ' + str(count) + ': '))
        video_file.write(str(run_time) + '\n') 
    video_file.close()
    print ('Времена сохранены в video_times.txt.')
main()
    
