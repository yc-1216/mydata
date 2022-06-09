import os

os.environ['CUDA_VISIBLE_DEVICES'] = '2'  # visible in this process + all children


SET_NAME = 'reviews_CDs_and_Vinyl_5.json.gz.stem.nostop/min_count5'
#SET_NAME = 'small_sample/min_count1'
PROGRAM_PATH = '/home/hlong/KBE4ExplainableRecommendation/Recommendation/'
DATA_PATH = '/home/hlong/KBE4ExplainableRecommendation/Amazon/'+SET_NAME+ '/'#'/min_count5/'

command = 'python ' + PROGRAM_PATH + 'main.py --data_dir ' + DATA_PATH
command += ' --train_dir ./tmp/'

INPUT_TRAIN_DIR = DATA_PATH + 'query_split/'
command += ' --input_train_dir ' + INPUT_TRAIN_DIR

command += ' --learning_rate 0.5'
command += ' --net_struct also_viewed_pv'
command += ' --L2_lambda 0.00'
command += ' --steps_per_checkpoint 100'
command += ' --max_train_epoch 10'
command += ' --batch_size 32'
command += ' --embed_size 10'

# 删除文件 linux
os.system('rm ./tmp/*')

print(command)
os.system(command)

print(command + ' --decode true' + ' --test_mode output_embedding')
os.system(command + ' --decode true' + ' --test_mode output_embedding')

print(command + ' --decode true' + ' --test_mode product_scores' + ' --similarity_func product')
os.system(command + ' --decode true' + ' --test_mode product_scores' + ' --similarity_func bias_product')
