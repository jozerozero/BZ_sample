import pyrubberband
import librosa
import soundfile as sf
import os
from glob import glob
import random
import shutil
from tqdm import tqdm


meta_new = open(os.path.join('ProsodyLabeling/tmp.txt'), mode='w', encoding='utf8')
pitch_list = [-2, -1.5, -1, 0, 1, 1.5, 2]


for meta in tqdm(open('ProsodyLabeling/000001-010000.txt', mode='r', encoding='utf8').readlines()):
	line = meta.strip().split('\t')
	if len(line) == 1:
		continue
	file_name = line[0]
	file_text = line[1]
	audio_path = os.path.join('Wave', file_name+'.wav')
	shutil.copyfile(os.path.join('Wave', file_name+'.wav'), os.path.join('sample', file_name+'.wav'))
	print(file_name+'\t'+file_text + '\n', file=meta_new)

	for j, i in enumerate(range(len(pitch_list)-1)):
		pitch_num = random.uniform(pitch_list[i], pitch_list[i+1])
		# print(pitch_num)
		new_file_name = file_name+'-'+str(j) + '.wav'
		y, sr = librosa.load(audio_path, sr=None)
		y_stretched = pyrubberband.pitch_shift(y, sr, pitch_num)
		# print(os.path.join('sample', new_file_name))
		if y.shape != y_stretched.shape:
			print('test')
		sf.write(os.path.join('sample', new_file_name), y_stretched, sr, format='wav')
		print(file_name+'-'+str(j)+'\t'+file_text + '\n', file=meta_new)
	# exit()	
	pass
