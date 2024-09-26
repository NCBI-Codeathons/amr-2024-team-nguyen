# AMR Model Phenotype Prediction Accuracies

**Species-antibiotic summary**

| |Ground Truth| |Expected| | |
|-|------------|-|--------|-|-|
|Species|F1 Score|Samples|F1 Score|95% CI||
|acinetobacter baumannii|0.8975|920|0.9328|0.9321|0.9335|
|campylobacter jejuni|0.9948|2138|0.9849|0.9847|0.9852|
|clostridioides difficile|0.0000|1|0.9678|#DIV/0!|#DIV/0!|
|enterococcus faecium|0.3406|14|0.9711|0.9707|0.9716|
|klebsiella pneumoniae|0.8497|469|0.8960|0.8952|0.8969|
|neisseria gonorrhoeae|0.5939|458|0.9640|0.9635|0.9645|
|pseudomonas aeruginosa|0.8398|324|0.7894|0.7873|0.7914|
|salmonella enterica|0.9230|7032|0.9319|0.9311|0.9327|
|staphylococcus aureus|0.8324|456|0.9764|0.9761|0.9767|
|streptococcus pneumoniae|0.9281|132|0.9629|0.9623|0.9634|

**All Species-antibiotic combinations**

| | |Ground Truth| |Expected| | |
|-|-|------------|-|--------|-|-|
|Species|Antibiotic|F1 Score|Samples|F1 Score|95% CI||
|acinetobacter baumannii|OVERALL|0.8975|920|0.9328|0.9321|0.9335|
|acinetobacter baumannii|amikacin|0.9054|992|0.9351|0.8997|0.9706|
|acinetobacter baumannii|ceftazidime|0.9125|1008|0.9112|0.8480|0.9744|
|acinetobacter baumannii|ciprofloxacin|0.9657|981|0.9802|0.9470|1.0135|
|acinetobacter baumannii|gentamicin|0.8331|1061|0.9238|0.8908|0.9567|
|acinetobacter baumannii|imipenem|0.9057|1018|0.9315|0.9126|0.9504|
|acinetobacter baumannii|levofloxacin|0.9044|843|0.9674|0.9215|1.0132|
|acinetobacter baumannii|meropenem|0.8908|611|0.9285|0.9064|0.9507|
|acinetobacter baumannii|tetracycline|0.9497|807|0.9517|0.9333|0.9701|
|acinetobacter baumannii|tobramycin|0.8107|963|0.8660|0.8387|0.8932|
|campylobacter jejuni|OVERALL|0.9948|2138|0.9849|0.9847|0.9852|
|campylobacter jejuni|ciprofloxacin|0.9931|2183|0.9846|0.9670|1.0021|
|campylobacter jejuni|nalidixic acid|0.9971|2049|0.9793|0.9370|1.0216|
|campylobacter jejuni|tetracycline|0.9940|2182|0.9910|0.9756|1.0063|
|clostridioides difficile|OVERALL|0.0000|1|0.9678|#DIV/0!|#DIV/0!|
|clostridioides difficile|moxifloxacin|0.0000|1|0.9678|0.9398|0.9957|
|enterococcus faecium|OVERALL|0.3406|14|0.9711|0.9707|0.9716|
|enterococcus faecium|ampicillin|0.4857|18|0.9800|0.9622|0.9978|
|enterococcus faecium|gentamicin|0.3750|10|0.9793|0.9439|1.0147|
|enterococcus faecium|linezolid|0.2800|18|0.9466|0.8917|1.0014|
|enterococcus faecium|streptomycin|0.1250|7|0.9881|0.9549|1.0212|
|enterococcus faecium|vancomycin|0.4375|18|0.9617|0.9442|0.9793|
|klebsiella pneumoniae|OVERALL|0.8497|469|0.8960|0.8952|0.8969|
|klebsiella pneumoniae|amikacin|0.8483|528|0.8705|0.8437|0.8973|
|klebsiella pneumoniae|aztreonam|0.8738|313|0.7951|0.7565|0.8336|
|klebsiella pneumoniae|cefazolin|0.8594|353|0.9284|0.9107|0.9462|
|klebsiella pneumoniae|cefepime|0.7256|473|0.7731|0.7344|0.8118|
|klebsiella pneumoniae|cefoxitin|0.6809|436|0.8382|0.7949|0.8814|
|klebsiella pneumoniae|ceftazidime|0.8956|1231|0.9072|0.8866|0.9278|
|klebsiella pneumoniae|ceftriaxone|0.9212|957|0.9462|0.9052|0.9871|
|klebsiella pneumoniae|cefuroxime|0.8773|117|0.9082|0.8567|0.9597|
|klebsiella pneumoniae|ciprofloxacin|0.8672|521|0.9371|0.9114|0.9628|
|klebsiella pneumoniae|ertapenem|0.9335|511|0.9254|0.8727|0.9781|
|klebsiella pneumoniae|gentamicin|0.8965|526|0.9438|0.9196|0.9680|
|klebsiella pneumoniae|imipenem|0.8759|343|0.9631|0.9561|0.9701|
|klebsiella pneumoniae|levofloxacin|0.8819|472|0.9261|0.8983|0.9540|
|klebsiella pneumoniae|meropenem|0.8701|531|0.9307|0.9047|0.9566|
|klebsiella pneumoniae|nitrofurantoin|0.5936|248|0.8103|0.7158|0.9048|
|klebsiella pneumoniae|tetracycline|0.8267|403|0.8786|0.8679|0.8894|
|klebsiella pneumoniae|tobramycin|0.8673|474|0.9488|0.9313|0.9664|
|klebsiella pneumoniae|trimethoprim|1.0000|9|0.8979|0.7767|1.0191|
|neisseria gonorrhoeae|OVERALL|0.5939|458|0.9640|0.9635|0.9645|
|neisseria gonorrhoeae|azithromycin|0.4972|454|0.9733|0.9537|0.9930|
|neisseria gonorrhoeae|cefixime|0.4640|461|0.9495|0.9152|0.9838|
|neisseria gonorrhoeae|ciprofloxacin|0.9069|462|0.9810|0.9646|0.9975|
|neisseria gonorrhoeae|tetracycline|0.5075|456|0.9521|0.8837|1.0205|
|pseudomonas aeruginosa|OVERALL|0.8398|324|0.7894|0.7873|0.7914|
|pseudomonas aeruginosa|amikacin|0.7744|260|0.7846|0.7153|0.8539|
|pseudomonas aeruginosa|aztreonam|0.8950|178|0.6168|0.5508|0.6827|
|pseudomonas aeruginosa|cefepime|0.8276|389|0.6436|0.5786|0.7087|
|pseudomonas aeruginosa|ceftazidime|0.8005|335|0.7803|0.7116|0.8489|
|pseudomonas aeruginosa|ciprofloxacin|0.9153|423|0.8698|0.8150|0.9247|
|pseudomonas aeruginosa|gentamicin|0.9041|405|0.8945|0.8169|0.9720|
|pseudomonas aeruginosa|imipenem|0.6769|355|0.7966|0.7489|0.8444|
|pseudomonas aeruginosa|levofloxacin|0.9017|275|0.8900|0.8387|0.9413|
|pseudomonas aeruginosa|meropenem|0.8065|233|0.7235|0.6780|0.7690|
|pseudomonas aeruginosa|tobramycin|0.8957|390|0.8940|0.8235|0.9644|
|salmonella enterica|OVERALL|0.9230|7032|0.9319|0.9311|0.9327|
|salmonella enterica|ampicillin|0.9551|8362|0.9066|0.9001|0.9130|
|salmonella enterica|cefoxitin|0.9658|8270|0.9543|0.9325|0.9762|
|salmonella enterica|ceftiofur|0.9870|4713|0.9745|0.9606|0.9884|
|salmonella enterica|ceftriaxone|0.9425|8277|0.9815|0.9714|0.9915|
|salmonella enterica|chloramphenicol|0.9738|8356|0.8683|0.8435|0.8931|
|salmonella enterica|ciprofloxacin|0.5119|8359|0.9468|0.9298|0.9638|
|salmonella enterica|gentamicin|0.9080|8354|0.9201|0.9090|0.9312|
|salmonella enterica|kanamycin|0.9153|3781|0.8359|0.7912|0.8805|
|salmonella enterica|nalidixic acid|0.9696|8338|0.9421|0.9018|0.9824|
|salmonella enterica|streptomycin|0.9099|8253|0.9318|0.9110|0.9526|
|salmonella enterica|sulfisoxazole|0.9796|7919|0.9867|0.9759|0.9974|
|salmonella enterica|tetracycline|0.9808|8352|0.9763|0.9630|0.9896|
|salmonella enterica|trimethoprim|1.0000|82|0.8896|0.8625|0.9167|
|staphylococcus aureus|OVERALL|0.8324|456|0.9764|0.9761|0.9767|
|staphylococcus aureus|cefoxitin|0.6118|33|0.9923|0.9836|1.0010|
|staphylococcus aureus|ciprofloxacin|0.9521|428|0.9896|0.9784|1.0009|
|staphylococcus aureus|clindamycin|0.9432|642|0.9711|0.9363|1.0060|
|staphylococcus aureus|erythromycin|0.8878|636|0.9810|0.9675|0.9945|
|staphylococcus aureus|fusidic acid|0.8117|271|0.9704|0.9513|0.9896|
|staphylococcus aureus|gentamicin|0.7386|642|0.9927|0.9780|1.0073|
|staphylococcus aureus|oxacillin|0.9434|638|0.9631|0.9461|0.9802|
|staphylococcus aureus|penicillin|0.7334|357|0.9509|0.9255|0.9763|
|staphylococcus aureus|tetracycline|0.8693|460|0.9763|0.9611|0.9916|
|streptococcus pneumoniae|OVERALL|0.9281|132|0.9629|0.9623|0.9634|
|streptococcus pneumoniae|cefuroxime|1.0000|50|0.9832|0.9545|1.0119|
|streptococcus pneumoniae|chloramphenicol|1.0000|50|0.9353|0.9016|0.9690|
|streptococcus pneumoniae|erythromycin|0.9849|188|0.9749|0.9582|0.9916|
|streptococcus pneumoniae|penicillin|0.6556|187|0.9562|0.9520|0.9603|
|streptococcus pneumoniae|tetracycline|1.0000|187|0.9647|0.9529|0.9766|
