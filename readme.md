# NeuralNets applied to $O^2$ volume in ramp test generated data

## Intro

My thesis is about models that are used in ramp test to evaluate if the Volume of $O_2$ gets to a max value or not, comunly called plateau. In this Repo I will not use those models, just solve again the same problems using other technics. The objective is inf and classify the position of the plateau.

| Class  | Presents Plateau                      | No Plateau                            |
| ------ | ------------------------------------- | ------------------------------------- |
| Images | ![readme_images/i3](readme_images/i3) | ![readme_images/i1](readme_images/i1) |

---

# Run yourself

## Data generated:

1.  run r script usint

         > Rscript the main_<>.r script

2.  run make_npz .py file

         > python make_npz_<>.r

## run simple model

3. Create or choose a notebook and test the data

# Early Results

## 1. Convolutional neural network

                     precision    recall  f1-score   support
                 0       0.94      0.97      0.96      1280
                 1       0.85      0.77      0.81       320
          accuracy                           0.93      1600
         macro avg       0.90      0.87      0.88      1600
      weighted avg       0.93      0.93      0.93      1600
      [[1238   42]
       [  74  246]]

## 2. Recurrent neural network

               precision    recall  f1-score   support
            0       0.98      0.96      0.97      1200
            1       0.95      0.97      0.96      1000
      accuracy                          0.96      2200
      macro avg     0.96      0.96      0.96      2200
      weighted avg  0.96      0.96      0.96      2200
     [[1148   52]
      [  28  972]]

---

## Future goals

1. Better data generation(First TODO):
   1. Add more segments to make diferents formats;
   2. Some images X not start on 0 (or left down for the image);
   3. Add zeros in start of sequences to noise the csv data;
   4. Make $\sigma^2$ vary;
   5. Divide train test before saving on folder.
2. Classify as imagem and find the position, in the image, of the plateau;
3. Same net using the sequence classify and regress return the position of the plateau.

## Data generator (Ramp test) \lastupdate11/06/22

- Noise:
  - Varyng X and Y plots and max;
  - Varyng sample sizes;
  - Varyng position of plateau relative to Xmax.

---

### Noises Applied in data generation to get more robust models

| Noise                                | Image                                 |
| ------------------------------------ | ------------------------------------- |
| Plateau, y-axis has been made higher | ![readme_images/i2](readme_images/i2) |
