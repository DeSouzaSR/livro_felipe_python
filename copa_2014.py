# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 18:11:52 2025

@author: srsouza


Programa: download de dados da Copa 2014
"""
import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print('Dowloaded {}'.format((time*BUFF_SIZE)/length)*100)


def download(response, output):
    total_dowloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_dowloaded += len(data)
        if not data:
            break
        output.write(data)
        print(f'Dowloaded {total_dowloaded}')


def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO('saida.zip', mode='w')
    
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    

if __name__ == '__main__':
    main()

 
