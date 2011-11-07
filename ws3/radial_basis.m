function [ std_dev ] = radial_basis( inputs, targets )
%RADIAL_BASIS Summary of this function goes here
%   Detailed explanation goes here
    nodes = 20;
    xsize = size(inputs);
    centres = randsample(inputs, 2);
    %augs1 = [inputs, centres(1)];
    %augs2 = [inputs, centres(2)];
    %extras = [80:80:3240] + 1
    augs = [inputs; repmat(centres(1), 1, xsize(2))]';
    dists = abs(augs(:, 1) - augs(:, 2));
    d_max = max(dists);
    std_dev = (-1 * nodes / d_max) * dists.^2;
    
    
end

