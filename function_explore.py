def func_explore (a2):
    plt.hist(a2)
    plt.axvline(a2.mean())
    plt.show()
    plt.boxplot(a2,showmeans=True)
    plt.show
    mean1=np.mean(a2)
    median1=np.median(a2)
    iqr1=iqr(a2)
    standev=np.std(a2)
    pcnt25=np.percentile(a2,25)
    pcnt75=np.percentile(a2,75)
    skewness = 3*(mean1 - median1)/standev
    HighOutLier = pcnt75 + 1.5*iqr1
    LowOutLier = pcnt25 - 1.5*iqr1
    print ("Mean :",  mean1)
    print ("Median :", median1)
    print ("IQR", iqr1)
    print ("Standard Deviation", standev)
    print ("25Percentile", pcnt25)
    print ("75Percentile", pcnt75)
    print ("Skewness", skewness)
    if skewness > 0:
        print ("Right Skewed")
    elif skewness <0:
        print ("Right Skewed")
    else:
        print ("Normal Distribution")
    print ("High Outlier Value", HighOutLier)
    print ("Low Outlier Value", LowOutLier)
    if np.max(a2) <=HighOutLier:
        print ("No Outlier on the high side")
    else:
        print ("Atleast one Outlier on the high side")
    if np.min(a2) >=LowOutLier:
        print ("No Outlier on the low side")
    else:
        print ("Atleast one Outlier on the low side")
    