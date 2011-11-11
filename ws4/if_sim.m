 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 % Simulation of (leaky) integrate-and-fire neuron
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 % Thomas Trappenberg, "Fundamentals of Computational Neuroscience", 2002
 % Some comments added by S O'Keefe 2008
 clear; clf;

 % parameters of the model
 tau_inv=0.1;    % inverse time constant 1/tau
 uu=0;           % initial membrane voltage is zero
 I_ext=12;       % constant external input
 theta=10;       % firing threshold

 % Integration with Euler method
 % 
 % The time increment each step is 1
 % The membrane resistance R is 1
 % if the cell membrane voltage > threshold, then the membrane voltage
 % at the next step only depends on the external current
 t_step=0;                      % set initial time point to zero
 for it=0:100                   % repeat loop for 101 values of it
     t_step=t_step+1;           % move to next time step
     x=uu<theta;                % logical variable = 0 if membrane voltage > threshold
     uu=x*(1-tau_inv)*uu+tau_inv*I_ext; % calculate membrane voltage
     u(t_step)=uu;              % remember the membrane voltage 
     t(t_step)=it;              % remember the time step
     s(t_step)=1-x;             % remember whether the cell spiked
 end

 subplot('position',[0.13 0.13 1-0.26 0.6])
   plot(t,u);
   hold on; plot([0 100],[10 10],'--');
   axis([0 100 0. 12])
   xlabel('time [\tau]');
   ylabel('u(t)')

 subplot('position',[0.13 0.8 1-0.26 0.1])
   plot(t,s,'.','markersize',20);
   axis([0 100 0.5 1.5])
   set(gca,'xtick',[],'ytick',[])
   ylabel('spikes')
