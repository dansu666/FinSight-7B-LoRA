# FinSight-7B Training Script
# Framework: Llama-Factory
# Base Model: Qwen2.5-7B-Instruct

llamafactory-cli train \
    --stage sft \
    --do_train \
    --model_name_or_path Qwen/Qwen2.5-7B-Instruct \
    --dataset fin_risk \
    --dataset_dir ./data \
    --template qwen \
    --finetuning_type lora \
    --lora_target all \
    --output_dir ./saves/FinSight-7B \
    --overwrite_output_dir \
    --cutoff_len 1024 \
    --preprocessing_num_workers 16 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 2e-4 \
    --num_train_epochs 5.0 \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.1 \
    --bf16 True \
    --plot_loss True \
    --report_to none