% Example usage of the service

addpath '/home/panton/docs/thesis-code/client/matlab'

g = goldmine('http://localhost:8080/service');
g.authenticate('admin', 'password');

sites = g.call('site.listing', {NaN});

for i = 1:length(sites)
    disp(sites{i}.name);
    for j = 1:length(sites{i}.cores)
       disp(['  - ' sites{i}.cores{j}.name]); 
    end
end
