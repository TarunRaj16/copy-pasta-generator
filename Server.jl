#!/usr/bin/env julia
using PyCall

unshift!(PyVector(pyimport("sys")["path"]), "")
@pyimport CopyPasta

function main()
    @async begin
        server = listen(3001)
        while true
            sock = accept(server)
            @async while true
                write(sock, CopyPasta.generate_copy_pasta(readline(sock)))
            end
        end
    end
end
