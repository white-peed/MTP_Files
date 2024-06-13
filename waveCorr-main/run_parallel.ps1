$network_models = "cs_CNN", "waveCorr", "cs_LSTM_CNN", "eiie"  # Replace with your model names
$datasets = "can_new"  # Replace with your dataset names
$seeds = 1111  # Replace with your seed values

foreach ($network_model in $network_models) {
    foreach ($dataset in $datasets) {
        foreach ($seed in $seeds) {
            Start-Process powershell -ArgumentList "-NoExit", "./venv/Scripts/activate.ps1; cd src; python wavecorr_run.py --network_model $network_model --seed $seed --dataset_name $dataset"
        }
    }
}
