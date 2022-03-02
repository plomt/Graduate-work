#!/bin/bash

# CONSTANTS-----------------------------------------------
ip=85.143.112.116
home_path=/home/lpa005
# --------------------------------------------------------

echo "Введите свой логин"
read login

echo "Введите название директории, в которой будем вести расчеты"
read dir_name

# создаем директорию на кластере
ssh ${login}@${ip} mkdir ${dir_name}

echo "путь куда кладем task.sh: ${home_path}/${dir_name}"
scp ./task.sh "${login}@${ip}:${home_path}/${dir_name}"

echo "путь куда кладем файл исполнения: ${home_path}/${dir_name}"
scp ./test "${login}@${ip}:${home_path}/${dir_name}"

echo "выполняем расчет"
ssh ${login}@${ip} "cd ${home_path}/${dir_name}; sbatch task.sh"

