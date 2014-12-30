class AddTitleAndVisitCountToVisits < ActiveRecord::Migration
  def change
    add_column :visits, :title, :string
    add_column :visits, :visit_count, :integer
  end
end
