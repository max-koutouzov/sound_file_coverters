import soundfile
import os

"""
Converts WAV files to 16 Bits to be used with MPC 2000XL

"""


def to_16bit_wav(input_path=None, output_file=None):
    data, samplerate = soundfile.read(input_path)
    soundfile.write(output_file, data, samplerate, subtype='PCM_16')


def convertAllFilesInDirectoryTo16Bit(directory):
    for file in os.listdir(directory):
        if file.lower().endswith('.wav'):
            name_solo = file.rsplit('.', 1)[0]
            print(directory + name_solo)
            data, samplerate = soundfile.read(directory + file)

            soundfile.write('C:\\Users\\maxko\\Desktop\\converted_files_2000xl\\' + name_solo + '_16BIT.wav',
                            data,
                            samplerate, subtype='PCM_16')
            print("converting " + file + "to 16 - bit")


def main():
    convertAllFilesInDirectoryTo16Bit(directory='C:\\Users\\maxko\\Desktop\\mpc_2000\\')


if __name__ == '__main__':
    main()
