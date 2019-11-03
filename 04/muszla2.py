side_leng = 30;
min_leng = 0.2;
angle = 15;
width = 1;

module turtle_spiral_by_times(t_before, times, side_leng, angle, width) {
    if(times != 0) {
        t_after = forward(turn(t_before, angle), side_leng * angle / 180 * 3.14159);
        polyline([get_xy(t_before), get_xy(t_after)], width);

        turtle_spiral_by_times(t_after, times - 1, side_leng, angle, width);
    } else {
        turtle_spiral(t_before, side_leng / 1.618, min_leng, angle, width);
    }

}

module turtle_spiral(t_before, side_leng, min_leng, angle, width) {
    if(side_leng > min_leng) {
        times = 90 / angle;
        turtle_spiral_by_times(t_before, 90 / angle, side_leng, angle, width);
    }
}

turtle_spiral(
    turtle(0, 0, 0), 
    side_leng, 
    min_leng, 
    angle, 
    width
);
