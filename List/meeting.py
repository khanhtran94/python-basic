attendees = ["Ken", "Alex", "Treasure"]
attendees.append("Ash")
attendees.extend(["Rob", "PLP"])
optional_invitees = ["Ben J", "Dave"]
potential_attendees = attendees + optional_invitees

print("There are ", len(potential_attendees), " people")
# join se gep cac element trong arr voi dau "," Thay dau , bang dau khac thi no se phep khac
to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)

print("To: ", to_line)
print("Cc: ", cc_line)