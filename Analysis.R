require("plotly")
require("data.table")
require("ggplot2")


completeData = na.omit(fread("complete.csv", nrows = 50000))
#Get all the unique subId's

completeData$date <-  as.Date(as.character(completeData$date), format = "%Y%m%d")
uniquename <- sort(unique(completeData$name))

rangeSlider = c(min(completeData$close),
                max(completeData$close))

#Generate buttons for dropdown 1 - SubId
buttonList1 = list()
for (i in uniquename)
{
  element =   list(
    method = "restyle",
    args = list("transforms[0].value" , i),
    label = i
  )
  buttonList1 = c(buttonList1, list(element))
}
columns <- colnames(completeData)
# 1st, 2nd and 5th columns --ActivityId, subId, timestamp

p <-
  plot_ly(data = completeData, transforms = list(
    list(
      type = 'filter',
      target =  ~ name,
      operation = "=",
      value = uniquename[1]
    )
  )) %>%
  add_trace(
    data = completeData,
    text = "time" ,
    type = 'scatter',
    mode = 'lines',
    x = completeData$date,
    y = completeData$close,
    visible = T
  )  %>%
  layout(data = completeData,
         updatemenus = list(
           # Dropdown 1
           list(x = 0.25,
                y = 1.15,
                
                buttons = buttonList1)
         ))
p
