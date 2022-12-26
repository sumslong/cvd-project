We built and tested the performance of our machine learning algorithm in R as
well as Python. This file contains the R code used. The random forest model 
with the top three variables of age, BMI, and systolic blood pressure (called
ap_hi in the dataset) resulted in the best performance, with an accuracy of 93%.

library(tidyverse)
library(MASS)
library(tidymodels)
library(ggfortify)
library(randomForest)
library(discrim)
library(klaR)
library(rpart.plot)
library(vip)
library(naivebayes)

data <- read_csv2("cardio_train.csv")
summary(data)

data$BMI <- (data$weight/10) / (data$height/100)^2

data$gender_cat <- cut(data$gender, breaks=c(0.5, 1.5, 2.5), labels = c("Female", "Male"))

data$cardio_cat <- cut(data$cardio, breaks=c(-0.5, 0.5, 1.5), labels = c("No Disease", "Disease"))

summary(data$cardio)

summary(data$cardio_cat)

data$age_years <- data$age / 365

data_clean <- data %>% drop_na() %>% dplyr::select(BMI, cardio_cat, age_years, ap_hi)

data_split <- initial_split(data_clean, prop = 0.75) #can play around with the proportion

data_train <- training(data_split)
data_test <- testing(data_split)

#RANDOM FOREST
rf_spec <- rand_forest(mtry = 4) %>% set_engine("ranger", importance = "impurity") %>% set_mode("classification")

rf_recipe <- recipe(cardio_cat ~ ., data = data_clean)

workflow_rf <- workflow() %>% add_model(rf_spec) %>%% add_recipe(rf_recipe)

fit_rf <- workflow_rf %>% fit(data_clean)

compare_pred <- augment(fit_rf, new_data = data_test)

compare_pred %>% conf_mat(truth = cardio_cat, estimate = .pred_class)

compare_pred %>% accuracy(truth = cardio_cat, estimate = .pred_class)

As tested in R, the random machine learning algorithm has an accuracy of 93%.
