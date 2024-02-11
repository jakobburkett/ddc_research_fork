import numpy as np
from chart import SymbolicChart, OnsetChart
from functools import reduce


def create_onset_charts(meta, song_features, frame_rate):
    charts = []
    for raw_chart in meta['charts']:
        metadata = (raw_chart['difficulty_coarse'], raw_chart['difficulty_fine'], raw_chart['type'], raw_chart['desc_or_author'])
        try:
            onset_chart = OnsetChart(song_metadata, song_features, frame_rate, metadata, raw_chart['notes'])
        except ValueError as e:
            print ('Error from {}: {}'.format(meta['title'].encode('ascii', 'ignore'), e))
            continue
        charts.append(onset_chart)

    return charts

def create_symbolic_charts(meta, song_features, frame_rate, sym_k):
    charts = []
    for raw_chart in meta['charts']:
        metadata = (raw_chart['difficulty_coarse'], raw_chart['difficulty_fine'], raw_chart['type'], raw_chart['desc_or_author'])
        try:
            if sym_k == None:
                sym_k = 1
            sym_chart = SymbolicChart(song_metadata, song_features, frame_rate, metadata, raw_chart['notes'], sym_k)
        except ValueError as e:
            print ('Error from {}: {}'.format(meta['title'].encode('ascii', 'ignore'), e))
            continue
        charts.append(sym_chart)

    return charts

def get_frame_rate(rates):
    x,y = rates.split(',')
    return float(x) / float(y)


# def get_song_data(song_metadata, song_feats, song_charts):
#     global song_data
#     class song_data: 
#         song_metadata = song_metadata
#         song_feats = song_feats
#         song_charts = song_charts
#     return song_data

class Song_data: 
    def __init__(self, song_metadata, song_feats, song_charts):
        self.song_metadata = song_metadata
        self.song_feats = song_feats
        self.song_charts = song_charts

if __name__ == '__main__':
    import argparse
    import pickle
    import glob
    import json
    import os

    parser = argparse.ArgumentParser()

    parser.add_argument('dataset_fps', type=str, nargs='+', help='')
    parser.add_argument('--out_dir', type=str, required=True, help='')
    parser.add_argument('--chart_type', type=str, choices=['onset', 'sym'], help='')
    parser.add_argument('--frame_rate', type=str, help='')
    parser.add_argument('--feats_dir', type=str, help='')
    parser.add_argument('--sym_k', type=int, help='')

    # parser.set_defaults(
    #     chart_type='onset',
    #     frame_rate='44100,441')

    parser.set_defaults(
        chart_type='sym',
        sym_k=1
    )

    args = parser.parse_args()

    frame_rate = 1.0
    if args.frame_rate:
        frame_rate = get_frame_rate(args.frame_rate)
        print('frame_rate: {}'.format(frame_rate))

    name_from_fp = lambda x: os.path.splitext(os.path.split(x)[1])[0]

    # Create outdir
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    # Parse dataset FPs
    ngood = 0
    nbad = 0
    
    for dataset_fp in args.dataset_fps:
        dataset_name = name_from_fp(dataset_fp)
        dataset_out_names = []
        with open(dataset_fp, 'r') as f:
            json_fps = f.read().splitlines()

            for json_fp in json_fps:
                json_name = name_from_fp(json_fp)

                with open(json_fp, 'r') as json_f:
                    meta = json.loads(json_f.read())
                song_metadata = {k: meta[k] for k in ['title', 'artist', 'offset', 'bpms', 'stops']}

                song_feats = None
                # print '{}'.format(args.feats_dir)
                print('executing {}'.format(json_name))
                if args.feats_dir:
                    song_feats_fp = os.path.join(args.feats_dir, '{}.pkl'.format(json_name))
                    with open(song_feats_fp, 'rb') as f:
                        song_feats = pickle.load(f)
                print('executed {}'.format(json_name))
                if args.chart_type == 'onset':
                    song_charts = create_onset_charts(meta, song_feats, frame_rate)
                    # song_data = Song_data(song_metadata, song_feats, song_charts)
                    # print(f'type of meta: {type(meta)}\ntype of song_feats: {type(song_feats)}\ntype of song_charts: {type(song_charts)}')
                    # song_data.song_data = (song_metadata, song_feats, song_charts)
                    song_data = (song_metadata, song_feats, song_charts)
                elif args.chart_type == 'sym':
                    song_charts = create_symbolic_charts(meta, song_feats, frame_rate, args.sym_k)
                    # song_data = Song_data(song_metadata, song_feats, song_charts)
                    # print(f'type of meta: {type(meta)}\ntype of song_feats: {type(song_feats)}\ntype of song_charts: {type(song_charts)}')
                    # song_data.song_data = (song_metadata, song_feats, song_charts)
                    song_data = (song_metadata, song_feats, song_charts)
                else:
                    raise NotImplementedError

                ngood += len(song_charts)
                nbad += len(meta['charts']) - len(song_charts)

                if len(song_data[2]) == 0:
                    print ('No charts')
                    continue

                out_name = '{}.pkl'.format(json_name)
                out_fp = os.path.join(args.out_dir, out_name)
                dataset_out_names.append(os.path.abspath(out_fp))
                with open(out_fp, 'wb') as f:
                    pickle.dump(song_data, f)
                

        with open(os.path.join(args.out_dir, '{}.txt'.format(dataset_name)), 'w') as f:
            f.write('\n'.join(dataset_out_names))

    print ('Parsed {} charts, {} passed {} failed'.format(ngood + nbad, ngood, nbad))
