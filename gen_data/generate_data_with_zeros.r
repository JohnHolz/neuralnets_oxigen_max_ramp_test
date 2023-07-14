naming_file <- function(j,i,ruidos){
    return(paste(ruidos,"/imr_",sub('\\.','_',as.character(j)),"_",i,".png",sep = ''))
}

write_plot <- function(df,i,j,ruidos,new_min){
    png(file = naming_file(j,i,ruidos))
    ruidos = 'ruidos'
    par(mar=c(0,0,0,0))
    y_lim = c(0,100)
    x_lim = c(new_min,14)
    plot(df,ylab="",xlab="", yaxt = "n",xaxt = "n",xlim = x_lim,ylim = y_lim,frame.plot=FALSE)
    dev.off()
}

generate_df <- function(pp){
    errors_mc = generate_errors(n = n_amostra,disturbs = disturbs)
    df = get_data(p=pp,n = n_amostra,errors = errors_mc) 
    return(df)
}

generate_ruido <- function(j){
    df = generate_df(j)
    start_size = sample(1:350,1)
    
    new_min = -(14*(start_size/800))
    x_ruido = runif(n = start_size,max = 0,min=new_min)
    y = rep(0,start_size)

    zero_df = data.frame(cbind(x_ruido,y))
    
    colnames(zero_df) <- colnames(df)[c(1,2)]
    new_zero_df = rbind(zero_df, df[-sample(x = 1:600,start_size),c(1,2)])
    return(new_zero_df)
}