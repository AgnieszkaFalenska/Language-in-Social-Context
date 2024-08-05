#!/bin/bash

set -ue

## Download data
DATA_DIR="../data/cmv/"

link="https://chenhaot.com/data/cmv/cmv.tar.bz2"
wget -nc -P $DATA_DIR $link

## Unpack data
if [ ! -d "$DATA_DIR/all" ]; then
    tar -xjf $DATA_DIR/cmv.tar.bz2 -C $DATA_DIR
fi

## Prepare files
train_file=$DATA_DIR/all/train_period_data.jsonlist.bz2
heldout_file=$DATA_DIR/all/heldout_period_data.jsonlist.bz2
data_file=$DATA_DIR/cmv.jsonlist

if [ ! -e $data_file ]; then
    python ./normalize_cmv.py $train_file $heldout_file $data_file 
fi

## Filter direct exchanges
data_for_analysis=$DATA_DIR/cmv.direct_replies.csv
python ./filter_direct_replies.py $data_file $DATA_DIR/topics.info $DATA_DIR/topics.txt $data_for_analysis