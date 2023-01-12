import pandas as pd
# pseudocode:
# for member...
#     for month ...
###First iteration###
# create monthly_anchor_weight = baseline weight (at the end of loop reset monthly_anchor_weight to equal monthly median weight)
# calculate percent weight difference between anchor_weight and metric_month 1 weights
# (or whatever the next metric month with weight data is)
# create flag "extreme_monthly_weight" to flag month_diff_1 weights that are < - 6% or > 6% from anchor_weight_month_diff_1
# create create monthly_median_wt = median of month 1 weights where extreme_monthly_weight == False
# reset anchor_weight to = monthly_median_wt where metric_month == current metric month + 1
# end of loop
###Second iteration###
# calculate percent weight difference between new anchor_weight and
# metric_month 2 weights (or whatever the next metric month with weight data is)
# flag "extreme_monthly_weights" for weights that are < - 6% or > 6% from anchor_weight_month_diff_1
# calculate monthly_median_wt for all weights in the metric_month where extreme_monthly_weight == False
# reset anchor_weight to = monthly_median_wt where metric_month == current metric month + 1
# end of loop
###Continue through month_diff_24?***
df_sample = pd.DataFrame({1:[23,4.3],2:[8, 8]})
member_list = sorted(df_sample[~df_sample['baseline'].isna()]['member_id'].unique())
df_sample['is_extreme_monthly_weight'] = False

for i, member in enumerate(member_list[:5]):
    #     print(member)
    df_this_member = df_sample[df_sample['member_id'] == member]
    member_baseline = df_this_member['baseline'].iloc[i]
    month_difference_min = df_this_member[df_this_member['month_diff'] != 0].sort_values('metric_date')[
        'month_diff'].min()
    month_difference = df_this_member.sort_values('metric_date')['month_diff'].unique()
    previous_month_difference = month_difference - 1

    for month in df_this_member['month_diff'].unique():

        ### Bin data by month
        df_this_member_this_month = df_this_member[df_this_member['month_diff'] == month]

        ### create anchor weight
        inclusion_rule = (df_sample['member_id'] == member) & (df_sample['month_diff'] == month)
        if month == month_difference_min:
            monthly_anchor_weight = member_baseline
            df_sample.loc[inclusion_rule, 'monthly_anchor_weight'] = member_baseline

        #       ### calculate percent weight difference between mothly_anchor_weight and monthly_binned_weights
        df_sample.loc[inclusion_rule, 'anchor_wt_diff'] = (abs(monthly_anchor_weight - df_this_member_this_month['weight']) / monthly_anchor_weight)

        anchor_wt_diff = df_sample[ df_sample[~df_sample['anchor_wt_diff'].isna()] ]['anchor_wt_diff']

        #         print(anchor_wt_diff)

        ### flag monthly_binned_weights that are < - 6% or > 6% from monthly_anchor_weight
        if anchor_wt_diff > 0.06:
            is_extreme_monthly_weight = True
#             df_sample.loc[inclusion_rule, 'is_extreme_monthly_weight'] = True


#         inclusion_rule = (df_sample['member_id'] == member) & (df_sample['month_diff']==month) & (df_sample['is_flagged_extreme_rate'] == False) & (df_sample['anchor_wt_diff'] <= .06)
#         if (month > month_difference_min) and (month<=24):
#             df_sample.loc[inclusion_rule, 'monthly_median_weight'] = np.median(monthly_binned_weights)
#             monthly_anchor_weight = df_this_member_this_month['monthly_median_weight']
#             df_sample.loc[inclusion_rule, 'monthly_anchor_weight'] = np.median(monthly_binned_weights)
