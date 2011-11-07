function [ nets, mses, outs ] = make_net( neurons, spreads, inputs, targets )
%MAKE_NET Summary of this function goes here
%   Detailed explanation goes here
    nets = {};
    values = struct('nets', {}, 'outs', [], 'mses', []);
    for i=1:size(spreads)
        nets(i) = newrb(inputs, targets, 0.0, spreads(i), neurons, 1);
        %outs(i) = sim(rb(i), inputs);
        %mses(i) = mse(targets - outs);
    end

end

