naming_file <- function(j,i){
    return(paste("images/im_",sub('\\.','_',as.character(j)),"_",i,".png",sep = ''))
}

write_plot <- function(df,i,j){
    y_lim = c(0,runif(1,90,130))
    png(file = naming_file(j,i),width = 360, height = 360)

    par(mar=c(0,0,0,0))
    plot(df[,c(1,2)],ylab="",xlab="", yaxt = "n",xaxt = "n",xlim = x_lim,ylim = y_lim,frame.plot=FALSE)

    dev.off()
}

generate_df <- function(p,n_amostra=800){
    errors_mc = generate_errors(n = n_amostra,disturbs = disturbs)
    df = get_data(p=p,n = n_amostra,errors = errors_mc) 
    return(df)
}