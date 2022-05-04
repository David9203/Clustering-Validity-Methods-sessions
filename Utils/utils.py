def calculateF1scoreclusters(y_test,y_predict,N_labels_real):
  for a in y_predict.unique():
      y_predict_aux=y_predict.copy()
      N_clase=[]
      indice_predict = y_predict_aux==a
      rows_test = y_test[indice_predict]
      for k in range(N_labels_real):
        N_clase.append(len(rows_test[rows_test==k])) #verifies if there is original value of labels in the row of the prediction
      y_predict[indice_predict] = N_clase.index(max(N_clase))
  report_entre = f1_score(y_test.to_list(), y_predict,average='micro')
  return(report_entre)
