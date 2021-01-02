df <- as.data.frame(table(airbnb$neigh_g))
df$per <- round((df$Freq/sum(df$Freq))*100, digits = 1)

neighbourhood_group <- df$Var1
Percent <- df$per
ypos <- cumsum(Percent)-0.5*Percent
ypos <- 100-ypos
ggplot()+ theme_bw() + geom_bar(aes(x="",y=Percent,fill= neighbourhood_group),
+                   stat="identity",color='white')+ 
+   coord_polar("y",start = 0)+ggtitle("Pie Chart of neigbourhood_group")+
+   theme(plot.title = element_text(hjust=0.7),axis.title=element_blank(),
+         axis.text=element_blank(),axis.ticks=element_blank(),
+         panel.border = element_blank(),panel.grid = element_blank())+
+   geom_text(aes(x="" ,y=ypos, label=paste0(Percent, "%")),size=3)