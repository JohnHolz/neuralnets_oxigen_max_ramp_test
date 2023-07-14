
generate_y_no_errors <- function(zeta0, zeta, betas, psis, x){
  tr <- zeta0 + zeta*x
  for(i in 1:length(psis)){
    tr <- tr + betas[i]*(x-psis[i])*as.numeric(x>psis[i])
  }
  return(tr)
}

generate_errors <- function(n,disturbs){
  return(rnorm(n=n,disturbs$mean,disturbs$sd))
}

generate_y_from_x <- function(x,params,n,disturbs,errors,p = .80){
  tr = generate_y_no_errors(zeta0 = params$zeta0,
                 zeta = params$zeta,
                 betas = params$betas,
                 psis = c(1, p*max(x)),
                 x = x) 
  y = tr + errors
  return(y)
}

get_data <- function(p,n = 800,errors = errors,params=params){
  xlim <- c(0,runif(1,12,16))
  x = sort(runif(n, xlim[1], xlim[2]))
  y = generate_y_from_x(x,params=params,n=n,disturbs=disturbs,p=p,errors = errors)
  df = data.frame(x,y)
  df$errors = errors
  return(df)
}

naming_file <- function(j,i,folder = 'csvs',extension='.csv'){
    return(paste(folder,"/file_",sub('\\.','_',as.character(j)),"_",i,extension,sep = ''))
}

generate_df <- function(p,n_amostra=800,disturbs,params){
    errors_mc = generate_errors(n = n_amostra,disturbs = disturbs)
    df = get_data(p=p,n = n_amostra,errors = errors_mc,params=params) 
    return(df)
}

write_csv <- function(df,i,j){
    write.csv(df[,c(1,2)], naming_file(i,j,'csvs','.csv'),row.names = FALSE)
}

write_plot <- function(df,i,j){
    y_lim = c(0,runif(1,94,130))
    x_lim=c(0,max(df$x))
    png(file = naming_file(j,i,'images','.png'),width = 360, height = 360)

    par(mar=c(0,0,0,0))
    plot(df[,c(1,2)],ylab="",xlab="", yaxt = "n",xaxt = "n",xlim = x_lim,ylim = y_lim,frame.plot=FALSE)

    dev.off()
}
