for i in $(seq 6 1 50)
do
       python run.py \
              --file_number ${i} \
              --source_file data/${i}_source.png \
              --mask_file data/${i}_mask.png \
              --target_file data/${i}_target.png \
              --output_dir results \
              #--gpu 0  --num_steps 1000 --save_video False
done
#python run.py \
 #      --source_file data/3_source.png \
  #     --mask_file data/3_mask.png \
   #    --target_file data/3_target.png \
    #   --output_dir results \
       #--gpu 0  --num_steps 1000 --save_video Flase

#python run.py \
 #      --source_file data/5_source.png \
  #     --mask_file data/5_mask.png \
   #    --target_file data/5_target.png \
    #   --output_dir results \
       #--gpu 0  --num_steps 1000 --save_video False





