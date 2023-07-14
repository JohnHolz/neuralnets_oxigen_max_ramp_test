source('gen_data/generate_data.r')

generate_images_function <- function(n_csvs){
    range = 8
    n = 800
    sgnf = 0.05
    p = c(.80,.85,.90,.95,1)

    ## mc
    MC_rep = 1000
    params = list(zeta0 = 11,
                    zeta = 25,
                    betas = c(-21,-4))
    disturbs = list(mean = 0,
                      sd = sqrt(11))

    for(j in p[-5]){
        for(i in 1:n_csvs){
            df = generate_df(j,800,disturbs=disturbs,params)
            write_csv(df,i,j)
        }
    print(j)
    }
    j=1
    for(i in 1:(n_csvs*5)){
            df = generate_df(j,800,disturbs,params)
            write_csv(df,i,j)
    }
}

folder_name = "csvs"
unlink(folder_name, recursive = TRUE)
dir.create(folder_name)

generate_images_function(2000)