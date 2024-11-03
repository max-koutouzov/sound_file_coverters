
import os
import soundfile as sf


"""
Convert .snd files to .wav files
This works on WSL and not on Windows PS.

Requirements:
pip install numpy
"""


def read_snd_file(input_file=None):
    """
    Read the .snd file
    :param input_file:
    :return:
    """
    data, samplerate = sf.read(file=input_file, dtype='int16')
    return data, samplerate


def write_wav(data=None, samplerate=None, filename=None):
    """
    Write the .wav file
    Bug: Converting MPC 2000xl files to WAV needed to be in 22050 sample rate.
    :param data:
    :param samplerate:
    :param filename:
    :return:
    """
    wav_out = sf.write(file=f'{filename.split(".")[0]}.wav',
                       data=data,
                       samplerate=22050)
    return wav_out


def list_files_in_dir(dir_path=None):
    """

    :param dir_path:
    :return:
    """
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return files


def main():
    snd_path = '/mnt/d/Akai_SND_files/'
    files = list_files_in_dir(dir_path=snd_path)
    for file in files:
        data, samplerate = read_snd_file(snd_path + file)
        write_wav(data=data, samplerate=samplerate, filename=snd_path + file)


if __name__ == '__main__':
    main()
